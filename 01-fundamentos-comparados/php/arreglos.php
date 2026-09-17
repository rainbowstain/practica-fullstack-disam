<?php
$montos = [60000, 8000, 25000, 10000, 500, 51000, 12000];
$mayores = [];

foreach ($montos as $monto) {
    if ($monto > 10000) {
        $mayores[] = $monto;
    }
}

print_r($mayores);
print_r($montos);

echo"Cantidad: " . count($mayores) . "\n";

foreach ($mayores as $mayor) {
    if ($mayor > 50000) {
        echo "$mayor - Director\n";
    } elseif ($mayor > 10000) {
        echo "$mayor - Jefe\n";
    } else {
        echo "Compra menor\n";
    }
}