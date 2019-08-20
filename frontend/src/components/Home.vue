<template>
  <div>
    <div>
      <select @change="filter(selected,priority,status)" v-model="selected">
        <option >all</option>
        <option v-for="option in options" v-bind:value="option.integration_id" :key="option">
          {{ option.name+" "+option.last_name }}
        </option>
      </select> 
       <select @change="filter(selected,priority,status)" v-model="priority">
        <option >all</option>
        <option v-for="option in list_prority" v-bind:value="option.text" :key="option">
          {{ option.text }}
        </option>
      </select> 
       <select  @change="filter(selected,priority,status)" v-model="status">
        <option >all</option>
        <option v-for="option in list_status" v-bind:value="option.text" :key="option">
          {{ option.text}}
        </option>
      </select>      
    </div>

    <div>
      <input type="text" v-model="id_interaction" placeholder="buscar">
      <button @click="filterInteraction(id_interaction)">filtrar</button>
    </div>

    <div>
    <table id="my_table">
      <thead>
        <tr>
          <th>assignee_id</th>          
          <th>interaction_id</th>
          <th>description</th>
          <th>priority</th>
          <th>status</th>
          <th>via</th>
          <th>requester</th>
        </tr>
      </thead>
      <tbody >
        <tr v-for="row in rows" :key="row"  >
          <td >{{row.assignee_id}}</td>
          <td>{{row.interaction_id}}</td>
          <td>{{row.description}}</td>
          <td>{{row.priority}}</td>
          <td>{{row.status}}</td>
          <td>{{row.via}}</td>
          <td>{{row.requester_id}}</td>
          
        </tr>
      </tbody>
    </table>
    </div>


    <div>
      <button v-on:click="importUsers()">importar usuarios</button>
      <input  type="text" v-model="num" placeholder="cantidad">
      <button v-on:click="createInteractions(num)">crear iteraciones</button> 
      <button v-on:click="importInteractions()">importar iteracciones</button>
      <!-- <button v-on:click="createPDF()">generar PDF</button>-->
    </div>

  </div>
</template>

<script>
//import jsPDF from 'jspdf'
//import 'jspdf-autotable'
import axios from 'axios'

export default {
  name: 'Home',

  data () {
    return {
      rows: [],
      options: '',
      selected:'all',

      list_status:[
      { text: 'open'},
      { text: 'pending'},
      { text: 'solved'}
      ],
      status:'all',

      list_prority:[
      { text: 'low'},
      { text: 'normal'},
      { text: 'high'},
      { text: 'urgent'}
      ],
      priority:'all',
      
      msg:'',
      id_interaction:'',
      num:0,
      counter:0
    }
  },

  methods: {
    /*
    createPDF(){
      alert('created')
      var doc = new jsPDF();
      doc.autoTable({html: '#my-table'});
      doc.save('table.pdf');
      alert('created')
    },*/

    getInteraction(){
      const path = 'http://localhost:5000/v1/interactions'
      axios.get(path).then((respuesta) =>{
        this.rows = respuesta.data
        counter =0
        console.log('algo esta pasando'+respuesta.data)
      })
      .catch((error) =>{
          console.error(error);
      })
    },

    getUser(){
      const path = 'http://localhost:5000/v1/users'
      axios.get(path).then((respuesta) =>{
        this.options = respuesta.data
        console.log('algo esta pasando'+respuesta.data)
      })
      .catch((error) =>{
          console.error(error);
      })
    },

    filter(id_user,id_priority,id_status){
      const path = 'http://localhost:5000/v1/filter'
      axios.get(path,{
        params: {
          id_user : id_user,
          id_status:id_status,
          id_priority:id_priority
        }
      }).then((respuesta) =>{
        this.rows = respuesta.data
        counter =0
        console.log('algo esta pasando'+respuesta.data)
      })
      .catch((error) =>{
          console.error(error);
      })
    },

    filterInteraction(id){
      const path = 'http://localhost:5000/v1/filter_interaction'
      axios.get(path,{
        params: {
          id_interaction : id
        }
      }).then((respuesta) =>{
        this.rows = respuesta.data
        counter =0
        console.log('algo esta pasando'+respuesta.data)
      })
      .catch((error) =>{
          console.error(error);
      })
    },

    importUsers(){
      const path = 'http://localhost:5000/v1/import_users'
      axios.get(path).then((respuesta) =>{
        this.rows = respuesta.data
        console.log('algo esta pasando'+respuesta.data)
      })
      .catch((error) =>{
          console.error(error);
      })
    },

    createInteractions(num){
      const path = 'http://localhost:5000/v1/create_interactions'
      axios.get(path,{
        params: {
          num : num
        }
      }).then((respuesta) =>{
        //this.rows = respuesta.data
        console.log('algo esta pasando'+respuesta.data)
      })
      .catch((error) =>{
          console.error(error);
      })
      alert('created interaction')
    },

    importInteractions(){
      const path = 'http://localhost:5000/v1/import_interactions'
      axios.get(path).then((respuesta) =>{
        this.rows = respuesta.data
        console.log('algo esta pasando'+respuesta.data)
      })
      .catch((error) =>{
          console.error(error);
      })
      window.location.reload()
    },

  },

  created () {
    this.getInteraction()
    this.getUser()
  }

}


</script>

<style scoped>
table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  text-align: left;
  padding: 8px;
}
tr:nth-child(even){background-color: #f2f2f2}
th {
  background-color:#008CBA;
  color: white;
}

button {
  background-color:#008CBA; /* Green */
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  display: block;
  font-size: 15px;
  width: 15%;
}

input{
  display: block;
}

input[type=text], select {
  width: 15%;
  padding: 12px 20px;
  margin: 8px 0;
  font-size: 15px;
  display: block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}
select{
display: inline-block;
}

</style>