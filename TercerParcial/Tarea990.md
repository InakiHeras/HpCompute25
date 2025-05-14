# Herramientas Open Source para Cómputo de Alto Desempeño

El **Cómputo de Alto Desempeño (HPC)** permite resolver problemas computacionalmente intensivos que no podrían abordarse de manera eficiente en equipos convencionales. Se aplica en áreas como simulaciones físicas, modelado climático, bioinformática, minería de datos, y entrenamiento de modelos de inteligencia artificial. El ecosistema de herramientas open source para HPC ha madurado hasta el punto de ser fundamental en la mayoría de centros de supercómputo y clústeres académicos e industriales.

A continuación, se describe una selección representativa de herramientas open source clasificadas por categoría, que facilitan el desarrollo, ejecución, monitoreo y mantenimiento de infraestructuras HPC.

---

## 🔧 Gestores de Clústeres y Recursos

Estas herramientas permiten la administración eficiente de los recursos computacionales, programando trabajos en colas, asignando CPU, memoria, GPU y almacenamiento según las políticas definidas.

### [Slurm](https://slurm.schedmd.com/documentation.html)
- Sistema de gestión de recursos y trabajos muy extendido en supercomputadoras.
- Compatible con arquitecturas heterogéneas (CPU, GPU, nodos especializados).
- Soporta planificación avanzada, preempción, backfilling y prioridad de usuarios.
- Integra herramientas para monitoreo en tiempo real, registros históricos y métricas.
- Altamente configurable y extensible mediante plugins.

### [OpenLava](https://github.com/FSchumacher/openlava/tree/2.0-release)
- Fork de LSF (Load Sharing Facility) de IBM, orientado a simplicidad y facilidad de uso.
- Permite colas de trabajos, control de políticas, y comandos similares a LSF.
- Útil en entornos educativos o pequeños clústeres, aunque con menor desarrollo reciente.

### [XCAT (Extreme Cloud Administration Toolkit)](https://xcat.org/)
- Plataforma para la gestión completa del ciclo de vida de un clúster HPC.
- Automatiza tareas como la provisión de nodos, instalación de sistemas operativos, configuración de redes y monitoreo.
- Usa un enfoque basado en plantillas y comandos centralizados (`xdsh`, `nodeset`).
- Compatible con arquitecturas bare-metal, virtuales y contenedores.

### [Grendel](https://grendel.readthedocs.io/en/stable/)
- Sistema de gestión emergente centrado en escalabilidad horizontal.
- Proporciona una interfaz RESTful para la administración de recursos y trabajos.
- Flexible y adaptable, ideal para plataformas HPC personalizadas o híbridas.

---

## 🔄 Sistemas de Flujo de Trabajo

Permiten definir, automatizar y escalar pipelines computacionales complejos, garantizando reproducibilidad, paralelismo y control de dependencias.

### [Nextflow](https://nextflow.io/)
- Basado en DSL para definir procesos modulares conectados mediante canales.
- Admite múltiples motores de ejecución (local, Slurm, Kubernetes, AWS Batch).
- Integra con Docker y Singularity; muy usado en bioinformática.
- Incluye repositorios como nf-core con pipelines validados por la comunidad.

### [Pegasus WMS](https://pegasus.isi.edu/)
- Sistema orientado a flujos de trabajo dirigidos por grafos acíclicos (DAG).
- Optimiza planificación, reutiliza tareas previas y maneja errores de forma robusta.
- Compatible con múltiples sistemas y entornos distribuidos.
- Usado en física, astronomía y bioinformática a gran escala.

---

## 📦 Gestión de Entornos y Paquetes

Estas herramientas abordan el problema de manejar múltiples versiones de software científico con diferentes configuraciones y dependencias.

### [Spack](https://spack.io/)
- Construye, instala y gestiona múltiples versiones de paquetes científicos.
- Compatible con arquitecturas y compiladores diversos.
- Usa recetas declarativas y se integra con módulos de entorno y contenedores.

### [EasyBuild](https://easybuild.io/)
- Automatiza construcción y despliegue de paquetes científicos.
- Usa archivos de configuración llamados *easyconfigs*.
- Enfocado en reproducibilidad y mantenimiento centralizado de software.

---

## ⚙️ Compiladores y Librerías de Cómputo

Herramientas esenciales para extraer el máximo rendimiento del hardware, optimizando código numérico y paralelo.

### [Intel HPC Compiler & OneAPI Toolkit](https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html#hpc-kit)
- Incluye compiladores (ICC, IFX), bibliotecas (MKL, MPI) y herramientas (VTune).
- Optimización avanzada para arquitecturas Intel (vectorización, afinidad, paralelismo).
- Gratis para uso académico bajo el modelo OneAPI.

### [NVIDIA HPC SDK](https://developer.nvidia.com/hpc-compilers)
- Incluye compiladores como `nvc++`, `nvfortran` con soporte CUDA, OpenMP, OpenACC.
- Compatible con bibliotecas aceleradas (cuBLAS, cuFFT, cuSolver).
- Incluye herramientas como Nsight Compute para análisis de rendimiento en GPU.

### [ArrayFire](https://arrayfire.org/docs/index.htm#gsc.tab=0)
- Librería de cómputo científico en GPU/CPU con API fácil de usar.
- Operaciones vectorizadas, visión por computadora, álgebra lineal, estadística.
- Disponible en C++, Python, Fortran, entre otros lenguajes.

---

## 📊 Benchmarks y Contenedores

Permiten evaluar el rendimiento del sistema HPC y facilitar despliegue reproducible de entornos computacionales.

### [OSU Micro-Benchmarks (OMB)](https://mvapich.cse.ohio-state.edu/benchmarks/)
- Microbenchmarks para evaluar latencia, ancho de banda y escalabilidad de bibliotecas MPI y PGAS.
- Útiles para comparar configuraciones de red, MPI y rendimiento de nodos.

### [Docker](https://www.docker.com/) + [Singularity (Apptainer)](https://apptainer.org/)
- Docker: contenedores ligeros para empaquetar entornos reproducibles.
- Singularity: diseñado para HPC multiusuario, ejecuta contenedores de forma segura en entornos compartidos.
- Usados junto a Slurm para flujos portables y consistentes.

