<?php

namespace exert\entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity
 * @ORM\Table(name="e_wechat_user")
 */
class WechatUserEntity
{
    /**
     * @ORM\Id
     * @ORM\GeneratedValue
     * @ORM\Column(type="integer", options={"unsigned"=true})
     * @var int
     */
    protected $id;

    /**
     * @ORM\Column(type="string", length=31)
     * @var string
     */
    protected $account;
}
