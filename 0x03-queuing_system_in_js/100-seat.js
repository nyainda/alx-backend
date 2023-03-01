import { createClient } from 'redis';
import { promisify } from 'util';
import express from 'express';
import { createQueue } from 'kue';

/** Variables and libraries */
const app = express();
const queue = createQueue();
const client = createClient();
let reservationEnabled;

/** Functions */
const reserveSeat = (number) => client.set('available_seats', number);
const getCurrentAvailableSeats = async () => {
  const availableSeatsPromise = promisify(client.get).bind(client);
  return await availableSeatsPromise('available_seats');
};

client.on('error', (err) =>
  console.log(`Redis client not connected to the server: ${err.message}`)
);
client.on('connect', () => {
  console.log('Client connected successfully');
  reserveSeat(50);
  reservationEnabled = true;
});

/** Endpoints */
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats();
  return res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled)
    return res.json({ status: 'Reservation are blocked' });
  const job = queue.create('reserve_seat', {}).save((err) => {
    if (!err) return res.json({ status: 'Reservation in process' });
    return res.json({ status: 'Reservation failed' });
  });
  job.on('complete', () =>
    console.log(`Seat reservation job ${job.id} completed`)
  );
  job.on('failed', (err) =>
    console.log(`Seat reservation job JOB_ID failed: ${err}`)
  );
});

app.get('/process', async (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats();
    console.log(currentAvailableSeats);
    if (currentAvailableSeats === 0) {
      reservationEnabled = false;
    }
    if (currentAvailableSeats >= 0) reserveSeat(currentAvailableSeats - 1);
    else {
      throw new Error('Not enough seats available');
      return;
    }
    done();
  });
  res.json({ status: 'Queue processing' });
});

const PORT = 1245;
app.listen(PORT, () => console.log(`Running server on Port ${PORT}`));
