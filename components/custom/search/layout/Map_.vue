<template>
  <div>

    <v-tabs
      class="my-5"
          v-model="tabs"
        >
          <v-tab
            v-for="(item, key) in items" :key="key"
            :href="`#${key}`"
            class="primary--text"
          >
            {{item.label}} ({{item.value.toLocaleString()}} {{$t("results")}})
          </v-tab>

          
        </v-tabs>
        
        <template v-if="item">

          <div class="text-right mb-2"><v-btn class="primary" :href="`${item.url}`" target="_blank">別タブで開く <v-icon class="ml-1">mdi-open-in-new</v-icon></v-btn></div>

          <template v-if="item.value > thres">
            <div class="pa-10 text-center" >
              <p>本画面で表示可能な検索結果数（{{thres.toLocaleString()}}件）を超えています。「別タブで開く」からアクセスしてください。</p>
            </div>
          </template>
          <template v-else>
        <iframe frameBorder="0" :src="`${item.url}&embedded=true`" style="width: 100%; height: 850px;"></iframe>
    </template>

    </template>

    
    <ul v-if="false">
      <li class="mb-2" v-for="(item, key) in items" :key="key">
        <a :href="item.url" target="_blank">
        {{item.label}} ({{item.value}})
        </a>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import { Prop, Vue, Component, Watch } from 'nuxt-property-decorator'
import ResultOption from '~/components/display/ResultOption.vue'

@Component({
  components: {
ResultOption
}
})
export default class FullTextSearch extends Vue {

  thres: number = 500

  tabs: any = ""

  prefix: string = "https://nakamura196.github.io/i3/map/?curation="
  //prefix: string = "http://localhost:3000/map/?curation="

  @Prop({})
  aggs!: any[]

  @Watch('aggs', { deep: true })
  watchTmp() {
    this.init()
  }

  mounted(){
    this.init()
  }

  items: any[] = []

  get item(){
    return this.items[Number(this.tabs)]
  }

  init(){

    this.tabs = "0"

    const query = this.$route.query

    let condition = ""

    
    for (const key in query) {
      const value = query[key]
      if (key.includes('[refinementList]')) {
        /*
        filters.push({
          label: key.split('[')[2].split(']')[0],
          value: query[key],
        })
        */
        condition += `&fc-${key.split('[')[2].split(']')[0]}=${value}`
      } else if (key.includes('[advanced]')) {
        /*
        advanced.push({
          label: key.split('[')[2].split(']')[0],
          value: query[key],
        })
        */
       condition += `&q-${key.split('[')[2].split(']')[0]}=${value}`
      } else if (key === "main[query]") {
        condition += `&q=${value}`
      }
    }

    ///////////////

    const aggs: any = this.aggs

    const arr = aggs["図"].value

    const settings: any = process.env.settings
    

    const map: any = {}

    for(const key in settings){
      map[settings[key].label] = key
    }

    const arr2 = []

    for(const obj of arr){
      const label = obj[0]
      const value = obj[1]
      const id = map[label]
      arr2.push({
        "id": id,
        "label": label,
        "value": value,
        "url": `${this.prefix}https://static.toyobunko-lab.jp/suikeichuzu_data/curation/${id}.json&label=分類,記号説明${condition}`
      })
    }

    this.items = arr2
  }
}
</script>
