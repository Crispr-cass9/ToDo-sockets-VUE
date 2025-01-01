<script lang="ts">
import { ref } from "vue";

interface Formulario{
  nombre: string;
  correo: string;
}


export default{
  setup() {
    const form = ref<Formulario>({
      nombre: '',
      correo: '',
    });
  

  const enviarDatos = async () => {
    console.log('Datos enviados:', form.value);
    
    try{
      await fetch('http://127.0.0.1:65432/iniciar-sesion',{
        method: 'POST',
        body: JSON.stringify(form.value)
      })
    }
    catch(e){
      console.error(e);
    }

    
  }

  return{
    form,
    enviarDatos
  }

  }
}
  

</script>

<template>
  <main>
    <form action="http://127.0.0.1:65432" method="POST">

      <label for="name">Nombre</label>
      <input type="text" v-model="form.nombre" name="name">
      
      <label for="name">Correo</label>
      <input type="text" v-model="form.correo" name="correo">
      
      <button @click.prevent.stop="enviarDatos()" type="submit" >Ingresar</button>
    </form>
  </main>
</template>
