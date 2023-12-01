# Tables: Slack Network analysis

## `message Table`

| `id` | `msg_type` | `msg_content` | `sender_name` | `msg_sent_time` | `msg_dist_type` | `time_thread_start` | `reply_count` | `reply_users_count `
| -----| --------------------- | --------------- | ------------------ | -------- | -------- | -------- | -------- | ----------- |
| Message Id (PK) | Message Type| Message Content  | Sender Name | Sent Time  | Message Type| Time When Thread Start| Count The Replies | Amount User Per Reply Count

## `Primary Key`

| `Columns`    |
| ------------ |
| Id |

## `Columns`
Some of import Columns with description
| `Label`         | `Name`         | `Type`                                 | `Nullable` | `Default`           | `Comment`            |
| --------------- | -------------- | -------------------------------------- | ---------- | ------------------- | -------------------- |
| Message ID      | id             | int auto_increment                     | `No`       |                     | Message ID           |
| Message Type    | msg_type       | varchar(100)                           | `No`       |                     | Department Name      |
| Message Content | msg_content    | varchar(100)                           | `No`       |                     | Parent Department    |
| Create Time     | CreateTime     | datetime                               | `No`       | current_timestamp() | Created Time         |


## `user Table`

| `id` | `user_id` | `user_name`
| -----| --------------------- | ---------------
| Id (PK) | User Id| User Name  |


## `Primary Key`

| `Columns`    |
| ------------ |
| Id |

## `Columns`
| `Label` | `Name`         | `Type`                | `Nullable`     | `Default`           | `Comment`            |
| ------------| -------------- | -------------     | -------------- | ------------------- | -------------------- |
| ID          | id             | int auto_increment| `No`           |                     | ID                   |
| User Id     | user_id        | int(FK)           | `No`           |                     | User ID              |
| User Name   | user_name      | varchar(100)      | `No`           |                     | User Name            |