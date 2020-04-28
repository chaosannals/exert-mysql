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
     * @ORM\Column(type="integer", options={"unsigned"=true})
     * @var int
     */
    protected $id;

    /**
     * @ORM\Column(type="string", length=31, unique=true, options={"comment"="用户名"})
     * @var string
     */
    protected $username;

    /**
     * @ORM\Column(type="binary", length=32, nullable=true, options={"comment"="密码"})
     * @var binary
     */
    protected $password;

    /**
     * @ORM\Column(type="string", length=31, nullable=true, options={"comment"="昵称"})
     * @var string
     */
    protected $nickname;

    /**
     * 性别
     * @ORM\Column(type="smallint", options={"comment"="性别"})
     */
    protected $gender;

    /**
     * @ORM\Column(name="enter_at", type="datetime", options={"comment"="录入日期"})
     * @var datetime
     */
    protected $enterAt;
}
