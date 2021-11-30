<template>
  <v-list>
    <v-subheader
      ><small>{{ $t('recentSearches') }}</small></v-subheader
    >
    <template v-for="(item, key) in items">
      <v-list-item
        :key="key"
        exact
        :to="localePath({ name: 'search', query: item.q })"
      >
        <v-list-item-title v-html="getText(item.q)"> </v-list-item-title>
      </v-list-item>

      <v-divider v-if="key < items.length - 1" :key="'d-' + key"></v-divider>
    </template>
  </v-list>
</template>

<!-- <div>
  </div> -->

<script lang="ts">
import { Prop, Vue, Component, Watch } from 'nuxt-property-decorator'
import { mdiMagnify, mdiClose } from '@mdi/js'

@Component({})
export default class FullTextSearch extends Vue {
  items: any = []

  key: any = process.env.BASE_URL

  @Watch('$route')
  watchRoute() {
    this.init()
  }

  init() {
    const key = this.key
    if (Object.prototype.hasOwnProperty.call(localStorage, key)) {
      const items = JSON.parse((localStorage as any).getItem(key))
      this.items = items
    } else {
      this.items = []
    }
  }

  mounted() {
    this.init()
  }

  getText(query: any) {
    let text = ''
    if (query.keyword) {
      let keyword = query.keyword
      if (typeof keyword === 'string') {
        keyword = [keyword]
      }
      text += keyword.join(' ')
    }
    for (let key in query) {
      if (key.includes('fc-') || key.includes('q-')) {
        let values = query[key]
        if (typeof values === 'string') {
          values = [values]
        }
        text +=
          ' ' +
          `<span style="color: #4caf50">${key
            .replace('fc-', this.$t('facet') + '-')
            .replace('q-', this.$t('detail') + '-')}</span>` +
          ': ' +
          values.join(', ')
      }
    }
    text = text.trim()

    if (!text) {
      text += `<span style="color: #4caf50">${this.$t('全件表示')}</span>`
    }
    return text
  }
}
</script>
