import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

const queue = kue.createQueue();

before(() => queue.testMode.enter());
afterEach(() => queue.testMode.clear());
after(() => queue.testMode.exit());

it('expect data in queue match with given data', () => {
  const testMockObject = [
    {
      phoneNumber: '1215151513',
      message: 'This is the code 1234 to verify your account',
    },
  ];
  createPushNotificationsJobs(testMockObject, queue);
  expect(queue.testMode.jobs[0].data.phoneNumber).to.equal('1215151513');
  expect(queue.testMode.jobs[0].data.message).to.equal(
    'This is the code 1234 to verify your account'
  );
});

it('expect data in queue match with given data if there is more than one element', () => {
  const testMockObject = [
    {
      phoneNumber: '1215151513',
      message: 'This is the code 1234 to verify your account',
    },
    {
      phoneNumber: '6241618111',
      message: 'This is the code 1234 to verify your account',
    },
  ];
  createPushNotificationsJobs(testMockObject, queue);
  expect(queue.testMode.jobs[1].data.phoneNumber).to.equal('6241618111');
  expect(queue.testMode.jobs[0].data.message).to.equal(
    'This is the code 1234 to verify your account'
  );
});

it('expect a message when there is no data', () => {
  expect(() => createPushNotificationsJobs({}, queue)).to.throw(
    'Jobs is not an array'
  );
});

it('expect a message when is given a null', () => {
  expect(() => createPushNotificationsJobs(null, queue)).to.throw(
    'Jobs is not an array'
  );
});
