import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) =>
  console.log(`Redis client not connected to the server: ${err.message}`)
);
client.on('ready', () => {
  console.log('Redis client connected to the server');
  client.hset('HolbertonSchools', 'PortLand', 50, print);
  client.hset('HolbertonSchools', 'Seattle', 80, print);
  client.hset('HolbertonSchools', 'Bogota', 20, print);
  client.hset('HolbertonSchools', 'Cali', 40, print);
  client.hset('HolbertonSchools', 'Paris', 2, print);
  client.hset('HolbertonSchools', 'New York', 20, print);
  client.hgetall('HolbertonSchools', (err, res) => {
    console.log(res);
  });
});
