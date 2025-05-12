# Herramientas Open Source para Cómputo de Alto Desempeño

El cómputo de alto desempeño es esencial para resolver problemas complejos en ciencia, ingeniería y análisis de daots a gran escala. A continuación, se presentan diversas herramientas open source que facilitan el desarrollo, ejecución y administración de cargas de trabajo HPC.

## **🔧 Gestores de Clústeres y Recursos**

### [Slurm](https://slurm.schedmd.com/documentation.html)
- Sistema de gestión de recusos y trabajo.
- Utilizado por muchos supercomputadores del mundo.
- Permite programación, monitoreo y asignación eficiente de recursos.

### [OpenLava](https://github.com/FSchumacher/openlava/tree/2.0-release)
- Derivado de Platform LSF, simplifica le gestión de tareas en clústeres
- Alternativa ligera a Slurm.

### [XCAT (Extreme Cloud Administration Toolkit)](https://xcat.org/)
- Automatiza el despliegue, administración y mantenimiento de clústeres HPC.

### [Grendel](https://grendel.readthedocs.io/en/stable/)
- Framework de gestión de recursos centrado en escalabilidad y eficiencia.
- Menos conocido, pero útil en entornos personalizados.

## 🔄 Sistemas de Flujo de trabajo

### [Nextflow](https://nextflow.io/)
- Framework para ejecutar flujos de trabajo reproducibles y escalables.
- Muy usado en bioinformática.

### [Pegasus WMS](https://pegasus.isi.edu/)
- Planificador de flujo de trabajo basago en DAGs.
- Permite ejecutar flujos complejos en entornos distribuidos.

## 📦 Gestión de Entornos y Paquetes

### [Spack](https://spack.io/)
- Gestor de paquetes especializado en HPC.
- Permite múltiples versiones, configuración y dependencias.

### [EasyBuild](https://easybuild.io/)
- Automatiza la construcción e instalación de software científico en clústeres.

## ⚙️ Compiladores y Librerías de Cómputo

### [Intel Compiler](https://www.intel.com/content/www/us/en/developer/tools/oneapi/toolkits.html#hpc-kit)
- Optimizaciones agresivas para arquitecturas Intel.
- Gratuito bajo licencia para uso académico y HPC.

### [NVidia HPC SDK](https://developer.nvidia.com/hpc-compilers)
- Conjunto de compiladores, librerías y herramientas para programación paralela (CUDA, OpenACC, OpenMP).

### [ArrayFire](https://arrayfire.org/docs/index.htm#gsc.tab=0)
- Librería de cómputo paralelo en GPU/CPU.
- Facilita operaciones vectoriales, estadística, visión por computadora, entre otras.

## 📊 Benchmarks y Contenedores

### [OSU Micro-Benchmarks](https://mvapich.cse.ohio-state.edu/benchmarks/)
- Conjunto de benchmarks para evaluar el rendimientos de bibliotecas MPI.

### [Docker](https://www.docker.com/)
- Contenedores ligeros para empaquetar y desplegar entornos HPC reproducibles.
- Útil junto con singularity en entornos HPC tradicionales.