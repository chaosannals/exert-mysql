<?php

namespace exert\command;

use ReflectionClass;
use exert\annotation\Seed;

class SeedCommand
{
    public static function grow()
    {
        $seedDir = realpath('./main/seed');
        $files = glob("$seedDir/*.php");
        foreach ($files as $file) {
            $name = basename($file, '.php');
            $class = "exert\\seed\\$name";
            if (!class_exists($class)) {
                continue;
            }

            $reflection = new ReflectionClass($class);
            if (!$reflection->isInstantiable()) {
                continue;
            }
            
            $instance = $reflection->newInstance();
            if (!method_exists($instance, 'grow')) {
                continue;
            }
            $instance->grow();
        }
    }
}
