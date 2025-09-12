<template lang="">
    <p>Product Details Page</p>
    <div class="grid grid-cols-2">
        <div> 
         <ProductCard  
              :name="doc.name"
              :image="doc.preview_image"
              :price="formatCurrency(doc.price, doc.currency)"
            /> 
        
        </div>
        <div>
        <!-- label="المدينه" -->
         <div class="p-2">
            <FormControl
                type="autocomplete"
                :options="[
                {
                    label: 'طرابلس',
                    value: '1',
                },
            
                ]"
                size="xl"
                variant="outline"
                placeholder="طرابلس"
                :disabled="false"
                label="المدينة"
                v-model="autocompleteValue"
            />
        </div>
        <div
            class="p-5"
            :required="true"
            >
            <FormControl
                :type="'text'"
                :ref_for="true"
                size="xl"
                variant="subtle"
                placeholder="القيمة"
                :disabled="false"
                v-model="city"
            />
        <div class="p-5">
            <FormControl
                type="checkbox"
                size="xl"
                variant="outline"
                placeholder="Placeholder"
                :disabled="false"
                label="عاوز توصيل ؟"
                v-model="delivery_request"
            />
        </div>
        </div>
    </div>

    </div>
    
</template>
<script setup>
import { createDocumentResource } from 'frappe-ui';
import { computed, ref } from 'vue';
import { useRoute } from 'vue-router'
import ProductCard from "../componets/ProductCard.vue"
const autocompleteValue = ref('طرابلس')
import { formatCurrency } from '../utils';
const route = useRoute()
const doc = computed( () => {
    return productDoc.doc
})
const productDoc = createDocumentResource({
    doctype: 'Product', // The DocType you want to fetch
    name: useRoute().params.name,
    auto: true
});
</script>
