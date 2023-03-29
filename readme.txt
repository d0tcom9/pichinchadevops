

El despliegue lo hice desde mi cuenta personal de AWS

Esta es la cadena de prueba

    curl -X POST -H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" -H "Content-Type: application/json" -d '{"message": "This is a test", "to": "Juan Perez", "from_": "Rita Asturia", "timeToLifeSec": 45}' http://devops-NLB-f5f4a57e0eef14cc.elb.us-east-1.amazonaws.com/DevOps

(en un pdf, dejo las pantallas con las pruebas)

Tuve que corregir la variable from y le puse from_ ya que me salía un mensaje de  variable reservada.

Creé un cluster en Amazon Web Services en Elastic Container Services (ECS) con Fargate, levanté 2 tasks (contenedores balanceados).


El balanceo lo hice con NLB y no con ALB considerando que luego se pueda enlazar a un API Gateway para configurar un dominio personalizado con https

Estoy revisando un curso de Terraform para poder desplegar toda esta infraestructura como código.