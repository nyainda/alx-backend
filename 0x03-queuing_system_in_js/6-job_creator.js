import { createQueue } from 'kue';

const queue = createQueue();

const jobObject = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const job = queue
  .create('push_notification_code', jobObject)
  .save((err) => !err && console.log(`Notification job created: ${job.id}`));

job.on('complete', (result) => console.log('Notification job completed'));
job.on('failed', (err) => console.log('Notification job failed'));
