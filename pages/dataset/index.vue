<template>
  <div>
    <Breadcrumbs :items="bh" />
    <v-container class="my-5 mb-10">
      <h2 class="mb-5">{{ title }}</h2>

      <v-data-table :headers="headers" :items="items" :items-per-page="-1">
        <template v-slot:item.dwn="{ item }">
          <v-btn icon :href="item['@id']" color="primary">
            <v-icon>mdi-file-download</v-icon>
          </v-btn>
        </template>

        <template v-slot:item.url="{ item }">
          <v-btn
            v-if="item.url"
            color="primary darken-2"
            rounded
            depressed
            class="my-2"
            :href="item.url"
            target="_blank"
            small
          >
            {{ $t('view') }}
            <v-icon class="ml-2">mdi-exit-to-app</v-icon>
          </v-btn>
        </template>
      </v-data-table>

      <v-btn
        v-if="false"
        class="my-10"
        rounded
        depressed
        color="primary darken-2"
        :to="localePath({ name: 'dictionary' })"
      >
        地名辞書
      </v-btn>
    </v-container>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'
import axios from 'axios'
import Breadcrumbs from '~/components/common/Breadcrumbs.vue'
@Component({
  components: { Breadcrumbs },
})
export default class Item extends Vue {
  title: any = this.$t('dataset')

  get headers(): any[] {
    return [
      {
        text: this.$t('name'),
        value: 'label',
      },
      {
        text: this.$t('format'),
        value: 'type',
      },
      {
        text: this.$t('download'),
        value: 'dwn',
      },
      {
        text: this.$t('viewer'),
        value: 'url',
      },
    ]
  }

  get items(): any[] {
    const items: any[] = []

    const baseUrl = process.env.BASE_URL

    items.push({
      '@id': `${baseUrl}/data/curation/top.json`,
      label: this.$t('iiif_curation'),
      type: this.$t('json'),
      url: `https://www.hi.u-tokyo.ac.jp/collection/digitalgallery/icv/?curation=${baseUrl}/data/curation/top.json`,
    })

    items.push({
      '@id': `${baseUrl}/api/data.ttl`,
      label: this.$t('metadata') + ' ' + this.$t('rdf'),
      type: this.$t('ttl'),
      url: `https://www.kanzaki.com/works/2014/pub/ld-browser?u=${baseUrl}/api/data.ttl`,
    })

    return items
  }

  get bh() {
    return [
      {
        text: this.$t('index'),
        disabled: false,
        to: this.localePath({ name: 'index' }),
        exact: true,
      },
      {
        text: this.title,
      },
    ]
  }
}
</script>
