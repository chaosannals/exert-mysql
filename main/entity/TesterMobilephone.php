<?php

namespace exert\entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity
 * @ORM\Table(
 *  name="e_tester_mobilephone",
 *  indexes={
 *      @ORM\Index(name="MOBILEPHONE_ID_INDEX", columns={"mobilephone_id"})
 *  }
 * )
 */
class TesterMobilephone
{
    /**
     * @ORM\Id
     * @ORM\Column(name="tester_id", type="integer", options={"unsigned"=true})
     * @var int
     */
    protected $testerId;

    /**
     * @ORM\Id
     * @ORM\Column(name="mobilephone_id", type="integer", options={"unsigned"=true})
     * @var int
     */
    protected $mobilephoneId;
}