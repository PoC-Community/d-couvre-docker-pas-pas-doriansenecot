SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

DROP DATABASE IF EXISTS epytodo;
CREATE DATABASE IF NOT EXISTS epytodo DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE epytodo;

DROP TABLE IF EXISTS user;
CREATE TABLE IF NOT EXISTS  user (
    `user_id` INT(6) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `username` CHAR(40) NOT NULL,
    `password` CHAR(255) NOT NULL
    );

DROP TABLE IF EXISTS task;
CREATE TABLE IF NOT EXISTS  task (
    `task_id` INT(6) NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `title` CHAR(40) NOT NULL,
    `begin` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `end` DATETIME DEFAULT NULL,
    `status` ENUM ('not started', 'in progress', 'done') NOT NULL DEFAULT 'not started'
    );

DROP TABLE IF EXISTS user_has_task;
CREATE TABLE IF NOT EXISTS user_has_task (
    `fk_user_id` INT(6) NOT NULL,
    `fk_task_id` INT(6)
    );
