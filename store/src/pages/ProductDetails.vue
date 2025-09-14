<template>
  <p>Product Details Page</p>

  <div class="grid grid-cols-2 gap-6">
    <!-- Left side: Product card -->
    <div>
      <ProductCard
        @select="orderDoc.submit()"
        :name="doc?.name"
        :image="doc?.preview_image"
        :price="formatCurrency(doc?.price, doc?.currency)"
        :buttonText="'تأكيد الطلب'"
        :loading="orderDoc.loading"
      />
    </div>

    <!-- Right side: Order form -->
    <div>
      <!-- City -->
      <div class="p-2">
        <FormControl
          type="autocomplete"
          :options="[
            { label: 'طرابلس', value: '1' },
            { label: 'بنغازي', value: '2' }
          ]"
          size="xl"
          variant="outline"
          placeholder="المدينة"
          label="المدينة"
          v-model="autocompleteValue"
        />
      </div>

      <!-- Required amount -->
      <div class="p-2">
        <FormControl
             :type="'number'"
           :ref_for="true"
          size="xl"
          variant="outline"
          placeholder="القيمة بالآلاف (مثال: 100 = 100 ألف)"
          label="القيمة المطلوبة"
           v-model="inputValue"
        />
      </div>

      <!-- Final total -->
      <div class="p-5">
        <FormControl
          label="القيمة النهائية بالدينار"
          type="text"
          size="xl"
          variant="subtle"
          placeholder="القيمة النهائية"
          v-model="grand_total"
          disabled
        />
      </div>

      <!-- Delivery request -->
      <div class="p-5">
        <FormControl
          type="checkbox"
          size="xl"
          label="عاوز توصيل ؟"
          v-model="delivery_request"
        />
      </div>
    </div>
  </div>

 
</template>

<script setup>
import { createDocumentResource, createResource } from 'frappe-ui'
import { computed, reactive, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import ProductCard from '../componets/ProductCard.vue'
import { formatCurrency } from '../utils'
import {useToast} from 'vue-toast-notification';
// form values 
const autocompleteValue = ref('طرابلس')
const inputValue = ref(0)
const grand_total = ref(0)
const delivery_request = ref(false)

// fetch product doc
const route = useRoute()
const productDoc = createDocumentResource({
  doctype: 'Product',
  name: route.params.name,
  auto: true,
})
const doc = computed(() => productDoc.doc)
// update grand total automatically
watch(inputValue, (val) => {
  if (doc.value.price) {
    grand_total.value = val * doc.value.price
  }
})
 
// create order

 // reactive items (always up-to-date)
const items = computed(() => {
  const qty = inputValue.value
  const rate = doc.value?.price || 0
  const total = qty * rate

  return [
    {
      // make sure keys match your child table: product, qty, rate, total
      product: "Bankak",
      qty,
      rate,
      total,
    }
  ]
})
import ToastPlugin from 'vue-toast-notification';
// order resource uses items.value so backend receives the latest values
const orderDoc = createResource({
  url: 'star_ecom.api.place_order',
  makeParams() {
    return {
      products: items.value,
      city: autocompleteValue.value,
      delivery_request: delivery_request.value
    }
  },
  onSuccess(order){
   const $toast = useToast();
  let instance = $toast.success('Order has Been Created ');
  }
})


 
 
</script>
