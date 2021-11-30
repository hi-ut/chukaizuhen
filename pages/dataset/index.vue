<template>
  <div>
    <Breadcrumbs :items="bh" />
    <v-container class="my-5">
      <h2 class="mb-5">{{ title }}</h2>

      <p class="mb-5">
        正保琉球国絵図デジタルアーカイブの地名をまとめて利用するためのデータセットを公開しています。
      </p>

      <v-data-table :headers="headers" :items="items">
        <template v-slot:item.dwn="{ item }">
          <v-btn icon :href="item['@id']" color="primary">
            <v-icon>mdi-file-download</v-icon>
          </v-btn>
        </template>

        <template v-slot:item.url="{ item }">
          <v-btn
            color="primary darken-2"
            rounded
            depressed
            class="my-2"
            :href="item.url"
            target="_blank"
          >
            {{ $t('view') }}
            <v-icon class="ml-2">mdi-exit-to-app</v-icon>
          </v-btn>
        </template>
      </v-data-table>
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
    return [
      {
        '@id':
          'https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/ryukyu/data/curation/0001.json',
        label: this.$t('正保琉球国絵図写'),
        type: this.$t('iiif_curation'),
        url:
          'https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/icv/?curation=https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/ryukyu/data/curation/0001.json',
      },
      {
        '@id':
          'https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/ryukyu/data/curation/0002.json',
        label: this.$t('正保琉球国悪鬼納島絵図写'),
        type: this.$t('iiif_curation'),
        url:
          'https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/icv/?curation=https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/ryukyu/data/curation/0002.json',
      },
      {
        '@id':
          'https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/ryukyu/data/curation/0003.json',
        label: this.$t('正保琉球国八山島絵図'),
        type: this.$t('iiif_curation'),
        url:
          'https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/icv/?curation=https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/ryukyu/data/curation/0003.json',
      },
    ]
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
