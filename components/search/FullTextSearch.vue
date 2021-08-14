<template>
  <div>
    <v-menu
      bottom
      offset-y
      nudge-bottom="20"
    >
      <template v-slot:activator="{ on, attrs }">
       <v-text-field
       autocomplete="off"
      v-model="q"
      light
      single-line
      filled
      rounded
      dense
      hide-details
      :label="$t('search')"
      label2="検索キーワードを入力"
      clearable
      clear-icon="mdi-close-circle"
      append-icon="mdi-magnify"
      :background-color="backgroundColor"
      @click:append="search"
      @keydown.enter="trigger"
      v-on="head ? on : false"
      placeholder="検索キーワードを入力"
    ></v-text-field>
      </template>

      <v-card>
        <v-list>
          <v-subheader><small>最近の検索</small></v-subheader>
          <v-list-item exact :to="localePath({name: 'search', query: item.q})" v-for="(item, key) in items" :key="key">
            <v-list-item-title>
              <template v-if="item.label === '全件表示'">
                <span style="color: #4CAF50;">
                {{item.label}}
                </span>
                </template>
                <template v-else>
                  {{item.label}}
                  </template>
              </v-list-item-title>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            :to="localePath({name: 'advanced'})"
            @click="menu = false"
          >
            {{$t("detail")}}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-menu>
  </div>
</template>

<script lang="ts">
import { Prop, Vue, Component, Watch } from 'nuxt-property-decorator'

let key: string = "search-suikeichuzu-history"

@Component({})
export default class FullTextSearch extends Vue {
  q: any = ''

  @Prop({default: "white"})
  backgroundColor!: string

  @Prop({default: false})
  head!: boolean

  @Watch('$route')
  watchRoute() {
    const query = this.$route.query
    if (query['main[query]']) {
      this.q = query['main[query]']
    }

    this.init()
  }

  trigger(event: any) {
    // 日本語入力中のEnterキー操作は無効にする
    if (event.keyCode !== 13) return
    this.search()
  }

  created() {
    const query = this.$route.query
    if (query['main[query]']) {
      this.q = query['main[query]']
    }
  }

  items: any[] = []

  init(){
    if(this.head){
      this.q = ""
    }
    

    if (Object.prototype.hasOwnProperty.call(localStorage, key)) {
      const items = JSON.parse(
        (localStorage as any).getItem(key)
      )
      this.items = items
    } else {
      this.items = []
    }
  }

  mounted(){
    this.init()
  }

  search() {
    let keywordStr = this.q

    if (!keywordStr) {
      keywordStr = ''
    } else {
      keywordStr = keywordStr.trim()
    }

    const keywords = this.$searchUtils.splitKeyword(keywordStr)

    // push 処理
    const query: any = Object.assign({}, this.$route.query)
    const values: string[] = []
    for (let i = 0; i < keywords.length; i++) {
      const keyword: any = keywords[i]
      if (keyword.label === 'keyword') {
        values.push(keyword.value)
      }
    }
    // query.keyword = values
    query['main[query]'] = keywordStr
    query["main[page]"] = 1

    const items = this.items

    const queries = []
    for(const item of items){
      queries.push(item.q["main[query]"])
    }

    if(queries.includes(keywordStr)){
      items.splice(queries.indexOf(keywordStr), 1)
    }

    items.unshift({
      label: keywordStr === "" ? "全件表示" : keywordStr,
      q: query
    })

    localStorage.setItem(key, JSON.stringify(items.slice(0, 5)))

    this.$router.push(
      this.localePath({
        name: 'search',
        query,
      }),
      () => {},
      () => {}
    )
  }
}
</script>
