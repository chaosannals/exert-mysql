<?php

namespace exert\entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity
 * @ORM\Table(name="e_wechat_nexus")
 */
class WechatNexus
{
    /**
     * @ORM\Id
     * @ORM\Column(type="string", length=31)
     * @var string
     */
    protected $unionid;

    /**
     * @ORM\Id
     * @ORM\Column(type="string", length=31)
     * @var string
     */
    protected $openid;

    /**
     * @ORM\Column(name="user_id", type="integer", options={"comment"="微信用户ID", "unsigned"=true})
     * @var int
     */
    protected $userId;

    /**
     * @ORM\Column(name="official_account_id", type="integer", options={"comment"="微信公众号ID", "unsigned"=true})
     * @var int
     */
    protected $officialAccountId;
}
