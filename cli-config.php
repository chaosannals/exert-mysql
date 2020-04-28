<?php

use Doctrine\ORM\Tools\Setup;
use Doctrine\ORM\EntityManager;
use Doctrine\DBAL\Driver\PDOMySql\Driver;
use Doctrine\ORM\Tools\Console\ConsoleRunner;

require_once __DIR__ . "/vendor/autoload.php";

$config = Setup::createAnnotationMetadataConfiguration(
    [__DIR__ . "/main"],
    true,
    null,
    null,
    false
);

$conn = [
    'driverClass' => Driver::class,
    'host'     => '127.0.0.1',
    'port'     => '3306',
    'user'     => 'admin',
    'password' => 'admin',
    'dbname'   => 'exert',
    'charset'  => 'utf8mb4',
    'driver_options' => [
        1002 => 'SET NAMES utf8mb4',
    ],
];

$entityManager = EntityManager::create($conn, $config);

return ConsoleRunner::createHelperSet($entityManager);
