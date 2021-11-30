<template>
  <div>
    <v-data-table
      :disable-sort="true"
      :headers="headers"
      :items="items2"
      hide-default-footer
      :items-per-page="-1"
    >
      <template v-slot:item.image="{ item }">
        <nuxt-link
          :to="
            localePath({
              name: 'item-id',
              params: { id: item.id },
            })
          "
        >
          <!-- query, -->
          <v-img
            contain
            max-height="90"
            max-width="90"
            style="height: 90px"
            width="100%"
            class="grey lighten-2 my-2"
            :src="item.image"
          />
        </nuxt-link>
      </template>

      <template v-slot:item.label="{ item }">
        <nuxt-link
          :to="
            localePath({
              name: 'item-id',
              params: { id: item.id },
            })
          "
        >
          {{ item.label }}
        </nuxt-link>
      </template>

      <template v-slot:item.拡大図="{ item }">
        <a
          rounded
          depressed
          target="_blank"
          color="primary darken-2"
          :href="`https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/icv/?curation=${
            item.curation
          }&xywh=${item.member.split('#xywh=')[1]}&mode=annotation&lang=ja`"
          >{{ $utils.formatArrayValue(item.図) }}
          <v-icon color="primary" class="ml-1">mdi-exit-to-app</v-icon></a
        >
      </template>
    </v-data-table>

    <v-simple-table class="mt-5" v-if="false">
      <template v-slot:default>
        <thead>
          <tr>
            <th></th>
            <th class="text-left">{{ $t('地名') }}</th>
            <th class="text-left">{{ $t('legend') }}</th>
            <th class="text-left">{{ $t('description') }}</th>
            <th class="text-left">{{ $t('拡大図') }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in items.hits" :key="item.id">
            <td class="py-2">
              <nuxt-link
                :to="
                  localePath({
                    name: 'item-id',
                    params: { id: item._id },
                  })
                "
              >
                <!-- query, -->
                <v-img
                  contain
                  max-height="90"
                  max-width="90"
                  style="height: 90px"
                  width="100%"
                  class="grey lighten-2"
                  :src="item._source.thumbnail"
                />
              </nuxt-link>
            </td>

            <td>
              <nuxt-link
                :to="
                  localePath({
                    name: 'item-id',
                    params: { id: item._id },
                  })
                "
                >{{ item._source.label }}</nuxt-link
              >
            </td>

            <td>
              {{ $utils.formatArrayValue(item._source.category) }}
            </td>

            <td>
              {{ $utils.formatArrayValue(item._source.description) }}
            </td>

            <td>
              <a
                rounded
                depressed
                target="_blank"
                color="primary darken-2"
                :href="`https://www.hi.u-tokyo.ac.jp/collection/degitalgallary/icv/?curation=${
                  item._source.curation
                }&xywh=${
                  item._source.member.split('#xywh=')[1]
                }&mode=annotation&lang=ja`"
                >{{ $utils.formatArrayValue(item._source.図) }}
                <v-icon color="primary" class="ml-1">mdi-exit-to-app</v-icon></a
              >
            </td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
  </div>
</template>

<script lang="ts">
import { Prop, Vue, Component, Watch } from 'nuxt-property-decorator'
import ResultOption from '~/components/display/ResultOption.vue'

@Component({
  components: {
    ResultOption,
  },
})
export default class FullTextSearch extends Vue {
  baseUrl: any = process.env.BASE_URL
  @Prop({})
  items!: any[]

  items3: any[] = [
    /*
    {
      name: 'あああ',
      legend: 'あいう',
    },
    {
      name: 'いいい',
      legend: 'あいう',
    },
    */
  ]
  headers: any[] = [
    {
      value: 'image',
    },
    {
      text: this.$t('地名'),
      value: 'label',
    },
    {
      text: this.$t('legend'),
      value: 'category',
    },
    {
      text: this.$t('description'),
      value: 'description',
    },
    {
      text: this.$t('拡大図'),
      value: '拡大図',
    },
  ]

  get items2(): any[] {
    const items: any[] = []
    const items2: any = this.items
    for (const item of items2.hits) {
      const obj: any = {
        id: item._id,
        label: item._source.label,
        image: item._source.thumbnail,
        category: this.$utils.formatArrayValue(item._source.category),
        description: this.$utils.formatArrayValue(item._source.description),
        curation: item._source.curation,
        member: item._source.member,
        図: this.$utils.formatArrayValue(item._source.図),
      }
      items.push(obj)
    }

    return items
  }

  getImage(list: any) {
    /*
    const index = '' + list[0]
    const markers = (process as any).env.legend
    if (markers[index] && index !== '0' && index !== '35') {
      return this.baseUrl + '/img/markers/' + index + '.png'
    } else {
      return ''
    }
    */
    return ''
  }

  getLegend(list: any) {
    /*
    const index = '' + list[0]
    const markers = (process as any).env.legend
    if (markers[index]) {
      const marker: any = markers[index]
      return marker.分類 + (marker.記号説明 ? ': ' : '') + marker.記号説明
    } else {
      return index
    }
    */
    return '1'
  }
}
</script>
