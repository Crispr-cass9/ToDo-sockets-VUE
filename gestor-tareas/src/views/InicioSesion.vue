<script lang="ts">
import { ref } from "vue";
import { useToast } from "vue-toastification";

const toast = useToast()

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
    
    try{
      console.log('Iniciando la funcion')
      const request = await fetch('http://127.0.0.1:65432/iniciar-sesion',{
        method: 'POST',
        body: JSON.stringify(form.value),
      })
      console.log(request)

      const data = await request.json()
      console.log('El status es el siguiente:', data.status)

      if (data.status != 'Ok'){
        toast.error('Un error ha ocurrido al iniciar sesión')
      }

      else {
        
      }

    }
    catch(e){
      console.log(e)
      toast.error('No se ha logrado iniciar sesión')
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
    
      <label for="name">Nombre</label>
      <input type="text" v-model="form.nombre" name="name">
      
      <label for="name">Correo</label>
      <input type="text" v-model="form.correo" name="correo">
      
      <button  @click="enviarDatos">Ingresar</button>
    
  </main>
</template>
