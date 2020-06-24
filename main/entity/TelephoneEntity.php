<?php

namespace exert\entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity
 * @ORM\Table(name="e_telephone")
 */
class TelephoneEntity
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer", options={"unsigned"=true})
     * @var int
     */
    protected $id;

    /**
     * @ORM\Column(type="string", length=15, unique=true)
     * @var string
     */
    protected $number;
}
