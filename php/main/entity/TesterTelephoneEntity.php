<?php

namespace exert\entity;

use Doctrine\ORM\Mapping as ORM;

/**
 * @ORM\Entity
 * @ORM\Table(
 *  name="e_tester_telephone",
 *  indexes={
 *      @ORM\Index(name="TELEPHONE_ID_INDEX", columns={"telephone_id"})
 *  }
 * )
 */
class TesterTelephoneEntity
{
    /**
     * @ORM\Id
     * @ORM\Column(name="tester_id", type="integer", options={"unsigned"=true})
     * @var int
     */
    protected $testerId;

    /**
     * @ORM\Id
     * @ORM\Column(name="telephone_id", type="integer", options={"unsigned"=true})
     * @var int
     */
    protected $telephoneId;
}
