<?php

namespace exert\entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity
 * @ORM\Table(name="e_tester")
 */
class Tester
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer")
     * @var int
     */
    protected $id;

    /**
     * @ORM\Column(type="string", length=31, unique=true, options={"comment"=""})
     * @var string
     */
    protected $username;

    /**
     * @ORM\Column(type="string")
     * @var string
     */
    protected $password;

    /**
     * @ORM\Column(type="string", length=31, nullable=true)
     * @var string
     */
    protected $nickname;

    /**
     * 性别
     * @Column(type="boolean")
     */
    protected $gender;

    /**
     * @ORM\Column(name="enter_at", type="datetime")
     * @var datetime
     */
    protected $enterAt;
}
