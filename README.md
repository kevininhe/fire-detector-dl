# fire-detector-dl
Aplicación de Deep Learning para la detección de incendios en imágenes satelitales.

#### ¿Cómo se ejecuta?
Una vez descargado el modelo pre-entrenado, instaladas las dependencias y copiado en la carpeta weights se ejecuta:

`streamlit run Introduccion.py`

Todas las dependencias se encuentran en el archivo de Docker.

#### Creación de imágen de docker
1. Instalar Docker.
2. Crear una cuenta en Docker Hub, y dentro de Docker hub crear un proyecto.
3. Desde la consola loguearse en DockerHub. Para eso se ejecuta:`sudo docker login`
4. Crear la imágen de docker. Para esto, una vez la consola está ubicada en la carpeta de este proyecto, se ejecuta: `sudo docker build -t <NombreUsuario>/<NombreProyectoDockerHub>:fire .`
5. Subir la imagen a Dockerhub. Para esto se ejecuta: `sudo docker push <NombreUsuario>/<NombreProyectoDockerHub>:fire`

Puede ejecutar la imagen localmente haciendo lo siguiente:

1. Ejecutar `sudo docker images` para ver las imágenes existentes, y de ahí tomar el id de la imagen más reciente.
2. Ejecutar:`sudo docker run -dp 9030:9030 <IdImagenReciente>`

#### Obtener la imagen en una MV de GCP o AWS
1. Instalar Docker en la máquina virtual. Ejecutar estos comandos uno por uno:

```
sudo apt -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common

curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list

sudo apt update

sudo apt install -y docker-ce docker-ce-cli containerd.io

docker -v
```
2. Agregar una regla de firewall en la máquina para que admita conexiones sobre el puerto 9030.
3. Loguearse en DockerHub. `sudo docker login`
4. Obtener la imagen cargada en DockerHub: `sudo docker pull <NombreUsuario>/<NombreProyectoDockerHub>:fire`
5. Ejecutar `sudo docker images` para ver las imágenes existentes, y de ahí tomar el id de la imagen más reciente.
6. Ejecutar:`sudo docker run -dp 9030:9030 <IdImagenReciente>`
7. Abrir en una pestaña aparte `<IpMaquinaVirtual>:9030`
