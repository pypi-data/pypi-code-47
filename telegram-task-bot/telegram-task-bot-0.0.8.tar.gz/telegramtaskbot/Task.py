import json
import logging
from abc import abstractmethod
from datetime import timedelta
from typing import List

import telegram
from telegram import InlineKeyboardButton
from telegram.ext import JobQueue


class Task(object):
    job_name: str
    job_start_name: str
    job_stop_name: str
    generic: bool = False  # defines if the task looks the same for each user
    first_time = 0
    repeat_time: timedelta = timedelta(seconds=5)
    filename: str = ''

    def __init__(self, job_queue: JobQueue):
        pass

    def start(self, jobs: List[telegram.ext.Job], update: telegram.Update, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=update.callback_query.message.chat_id,
                                 text=f'Setting the job {self.job_name} up')
        self._start(jobs, context.job_queue, update.callback_query.message.chat_id)

    def _start(self, jobs: List[telegram.ext.Job], job_queue: JobQueue, chat_id):
        new_job = job_queue.run_repeating(self.callback, self.repeat_time, context=chat_id, first=self.first_time)
        new_job.name = self.job_name
        jobs.append(new_job)

    def stop(self, jobs: List[telegram.ext.Job], update: telegram.Update, context: telegram.ext.CallbackContext):
        num_jobs = len(jobs)
        chat_id = update.callback_query.message.chat_id
        count = 0
        jobs_to_stop = [job for job in jobs if (job.context == chat_id and job.name == self.job_name)]
        for job_to_stop in jobs_to_stop:
            job_to_stop.schedule_removal()
            count += 1
            idx = jobs.index(job_to_stop)
            jobs.pop(idx)
        logging.info(f' stopped {count} of {num_jobs} jobs for chat_id={chat_id}')

    @abstractmethod
    def callback(self, context: telegram.ext.CallbackContext):
        context.bot.send_message(chat_id=context.job.context, text=f'Callback from {self.job_name}')

    def get_inline_keyboard(self):
        return [InlineKeyboardButton(f"Start {self.job_name} task", callback_data=self.job_start_name),
                InlineKeyboardButton(f"Stop {self.job_name} task", callback_data=self.job_stop_name),
                ]

    def save_user(self, user: str):
        users = self.load_users()
        users.append(user)
        final_users = list(set(users))
        self.save_to_json(final_users)

    def save_to_json(self, users):
        data = {'users': users}
        with open(self.filename + '.json', 'w') as outfile:
            json.dump(data, outfile)
        logging.info('Saved User')

    def load_users(self):
        try:
            with open(self.filename + '.json') as json_file:
                data = json.load(json_file)
                users = data['users']
        except IOError:
            users = []
            logging.info("File not accessible")
        finally:
            return users
