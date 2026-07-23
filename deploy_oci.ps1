# Script de deploy para OCI - Oracle Cloud Infrastructure
# Ejecutar en la terminal de OCI Cloud Shell o localmente con OCI CLI instalado

Write-Host "=======================================" -ForegroundColor Cyan
Write-Host "  Deploy BimBam Buy Agent en OCI" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

# Configuracion - CAMBIAR ESTOS VALORES
$COMPARTMENT_OCID = "ocid1.compartment.oc1..xxxxxxxxxxxx"  # Tu compartment OCID
$INSTANCE_NAME = "bimbam-buy-agent"
$SHAPE = "VM.Standard.E2.1.Micro"  # Free tier eligible
$SUBNET_OCID = "ocid1.subnet.oc1..xxxxxxxxxxxx"  # Tu subnet OCID

Write-Host "Paso 1: Crea una instancia de compute en OCI" -ForegroundColor Yellow
Write-Host "Ve a OCI Console -> Compute -> Instances -> Create Instance"
Write-Host "  Nombre: bimbam-buy-agent"
Write-Host "  Image: Canary Linux 9" 
Write-Host "  Shape: VM.Standard.E2.1.Micro (gratis)"
Write-Host "  VCN: Crea o selecciona una con puerto 8080 abierto"
Write-Host "  SSH keys: Agrega tu llave publica SSH"
Write-Host ""

Write-Host "Paso 2: Conectate por SSH y ejecuta los siguientes comandos:" -ForegroundColor Yellow
Write-Host ""
Write-Host "# Actualizar e instalar dependencias"
Write-Host "sudo dnf update -y"
Write-Host "sudo dnf install -y python3 python3-pip git"
Write-Host ""
Write-Host "# Clonar el repo"
Write-Host "git clone https://github.com/JazMendez17/challenge-alura-agente.git"
Write-Host "cd challenge-alura-agente"
Write-Host ""
Write-Host "# Instalar pip y dependencias"
Write-Host "pip3 install -r requirements.txt"
Write-Host ""
Write-Host "# Crear servicio systemd para que corra siempre"
Write-Host "sudo tee /etc/systemd/system/bimbam.service << 'EOF'"
Write-Host "[Unit]"
Write-Host "Description=BimBam Buy RAG Agent"
Write-Host "After=network.target"
Write-Host ""
Write-Host "[Service]"
Write-Host "User=opc"
Write-Host "WorkingDirectory=/home/opc/challenge-alura-agente"
Write-Host "ExecStart=/usr/bin/python3 /home/opc/challenge-alura-agente/app/app.py"
Write-Host "Restart=always"
Write-Host ""
Write-Host "[Install]"
Write-Host "WantedBy=multi-user.target"
Write-Host "EOF"
Write-Host ""
Write-Host "# Iniciar servicio"
Write-Host "sudo systemctl daemon-reload"
Write-Host "sudo systemctl enable bimbam"
Write-Host "sudo systemctl start bimbam"
Write-Host "sudo systemctl status bimbam"
Write-Host ""
Write-Host "Paso 3: Abrir puerto 8080 en el firewall de OCI" -ForegroundColor Yellow
Write-Host "  - Ve a Networking -> Virtual Cloud Networks"
Write-Host "  - Selecciona tu VCN -> Security Lists"
Write-Host "  - Agrega regla de ingreso:"
Write-Host "    Source: 0.0.0.0/0"
Write-Host "    Destination Port: 8080"
Write-Host "    Protocol: TCP"
Write-Host ""
Write-Host "Paso 4: Acceder a la app" -ForegroundColor Yellow
Write-Host "  URL: http://<IP_PUBLICA_DE_TU_INSTANCIA>:8080"
Write-Host ""
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host "  Alternativa: Usar Docker" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "# Si prefieres Docker, en la instancia OCI ejecuta:"
Write-Host "sudo dnf install -y docker"
Write-Host "sudo systemctl start docker"
Write-Host "sudo docker build -t bimbam-agent /home/opc/challenge-alura-agente"
Write-Host "sudo docker run -d -p 8080:8080 --name bimbam bimbam-agent"
Write-Host ""
