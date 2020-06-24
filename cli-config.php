<?php

use Doctrine\ORM\Tools\Setup;
use Doctrine\ORM\EntityManager;
use Doctrine\DBAL\Driver\PDOMySql\Driver;
use Doctrine\ORM\Tools\Console\ConsoleRunner;
use Dotenv\Dotenv;

require_once __DIR__ . "/vendor/autoload.php";

$dotenv = Dotenv::createMutable(__DIR__);
$dotenv->load();

$config = Setup::createAnnotationMetadataConfiguration(
    [__DIR__ . "/main"],
    true,
    null,
    null,
    false
);

$conn = [
    'driverClass' => Driver::class,
    'host'     => $_ENV['DB_HOST'] ?? '127.0.0.1',
    'port'     => $_ENV['DB_PORT'] ?? '3306',
    'user'     => $_ENV['DB_USER'] ?? 'root',
    'password' => $_ENV['DB_PASS'] ?? 'root',
    'dbname'   => $_ENV['DB_NAME'] ?? 'exert',
    'charset'  => 'utf8mb4',
    'driver_options' => [
        1002 => 'SET NAMES utf8mb4',
    ],
];

$entityManager = EntityManager::create($conn, $config);

return ConsoleRunner::createHelperSet($entityManager);
