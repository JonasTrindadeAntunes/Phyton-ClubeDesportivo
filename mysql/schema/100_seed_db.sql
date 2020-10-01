DROP DATABASE IF EXISTS `example_db`;
CREATE DATABASE `example_db` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;

USE `example_db`;

-- Create atletas table
DROP TABLE IF EXISTS `atletas`;
CREATE TABLE `atletas` (
    `id` INT (11) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `numidenticivil` INT (11),
    `nome` VARCHAR (40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci,
    `genero` VARCHAR (40) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci,
    `idade` INT (11),
    `atividade` VARCHAR (256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci,
    `fcr` INT (11),
    `premios` INT (11),
    `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE = InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET = utf8mb4 DEFAULT COLLATE utf8mb4_unicode_520_ci;
