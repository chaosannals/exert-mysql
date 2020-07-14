<?php

namespace exert\handle;

use Doctrine\Common\Annotations\AnnotationReader;
use Doctrine\Common\Annotations\AnnotationRegistry;

abstract class AnnotationHandle
{
    public static $reader;

    public static function getClassAnnotation($reflection, $annotation)
    {
        return self::$reader->getClassAnnotation($reflection, $annotation);
    }

    public static function getClassAnnotations($reflection)
    {
        return self::$reader->getClassAnnotations($reflection);
    }
}

AnnotationRegistry::registerLoader("class_exists");
AnnotationRegistry::registerAutoloadNamespace("exert", dirname(__DIR__));
AnnotationHandle::$reader = new AnnotationReader();
