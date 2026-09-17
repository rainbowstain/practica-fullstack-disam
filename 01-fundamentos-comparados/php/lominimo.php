<?php

$nombre = "Eduardo";
$monto = 30000;

echo "Hola $nombre\n";
echo 'Hola $nombre\n';
echo "Monto: " . $monto . "\n";

if ($monto > 50000) {
    echo "Director\n";
} elseif ($monto > 10000) {
    echo "Jefe\n";
} else {
    echo "Compra menor\n";
}
