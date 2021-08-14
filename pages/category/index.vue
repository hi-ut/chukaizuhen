<template>
  <div>
    <v-sheet color="grey lighten-2">
      <v-container fluid class="py-4">
        <v-breadcrumbs class="py-0" :items="bh">
          <template #divider>
            <v-icon>mdi-chevron-right</v-icon>
          </template>
        </v-breadcrumbs>
      </v-container>
    </v-sheet>
    <v-container class="my-5">
      <h2 class="mb-5">{{ $t('category') }}</h2>

      <v-simple-table>
        <template v-slot:default>
          <thead>
            <tr>
              <th>{{$t("name")}}</th>
              <!-- <th></th> -->
            </tr>
          </thead>
          <tbody>
            <template v-for="(agg, key) in aggs">
            <tr  :key="key" v-if="!agg.hide">
              <td>
                <nuxt-link
                    :to="
                      localePath({
                        name: 'category-slug',
                        params: {slug: key}
                      })
                    "
                  >
                    {{agg.label}}
                    </nuxt-link>
                    </td>

                    <!--
                    <td>
                      {{100}} {{$t("results")}}
                    </td>
                    -->
                    </tr>
                    </template>
                    </tbody>
                    </template>
      </v-simple-table>
                    

      
    </v-container>

    
  </div>
</template>

<script>
import axios from 'axios'


export default {
  components: {},
  data() {
    return {

      aggs: process.env.aggs,

      bh: [
        {
          text: this.$t('top'),
          disabled: false,
          to: this.localePath({ name: 'index' }),
          exact: true,
        },
        {
          text: this.$t('category'),
        },
      ]
    }
  },

  

  
  head() {
    return {
      title: this.$t('category'),
    }
  },
}
</script>
