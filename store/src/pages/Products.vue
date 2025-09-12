<template>
  <div class="max-w-3xl py-12 mx-auto">
    <h2 class="font-bold text-lg text-gray-600 mb-4">
      Welcome {{ session.user }}!
    </h2>
      <p class="text-gray-500 mb-6">
        تصفح منتجاتنا واختر ما يناسبك
      </p>
     
     <div v-if="products.list.data" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"> 
           <ProductCard class="grid-rows-3"
            v-for="data in products.list.data"
            :key="data.name"
            :name="data.name"
            :image="data.preview_image"
            :price="formatCurrency(data.price, data.currency)"
            /> 
          
     </div>
     



    <div class="flex flex-row space-x-2 mt-4">
      <Button @click="showDialog = true">Open Dialog</Button>
      <Button @click="session.logout.submit()">Logout</Button>
    </div>

    <!-- Dialog -->
    <Dialog title="Title" v-model="showDialog"> Dialog content </Dialog>
  </div>
</template>

<script setup>
import { Dialog } from "frappe-ui"
import { createListResource } from "frappe-ui"
import { ref } from "vue"
import { session } from "../data/session"
import ProductCard from "../componets/ProductCard.vue"
import { formatCurrency } from "../utils"
 
 
const products = createListResource({
  doctype: 'Product', // The DocType you want to fetch
  fields: [ 'name' , 'preview_image' , 'price' , 'currency' ], // Fields to retrieve
   orderBy: 'creation desc',
   auto: true,
});

const showDialog = ref(false)



</script>
