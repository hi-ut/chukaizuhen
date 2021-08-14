<template>
  <v-app>
    <div>
      <v-navigation-drawer v-model="drawer" app :temporary="true">
        <v-list>
        <v-list-item
          v-for="(item, key) in menu"
          :key="key"
          :to="item.to"
          :href="item.href"
          link
        >
          <v-list-item-action v-if="item.icon">
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <span>{{ $t(item.label) }}</span>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      </v-navigation-drawer>

      <v-app-bar dark>
        <v-app-bar-nav-icon v-if="isMobile" @click.stop="drawer = !drawer" />
        <v-toolbar-title>
          <nuxt-link
            :to="
              localePath({
                name: 'index',
              })
            "
            style="color: inherit; text-decoration: inherit"
          >
            {{ title }}
          </nuxt-link>
        </v-toolbar-title>

        <template v-if="$vuetify.breakpoint.name != 'xs'">
          <div class="ml-10">
            <FullTextSearch :head="true"/>
          </div>
        </template>

        <v-spacer></v-spacer>

        <template v-if="!isMobile">
          <v-btn
            v-for="(item, key) in menu"
            :key="key"
            class="ma-1"
            text
            depressed
            :to="item.to"
            :href="item.href"
            exact
          >
            <v-icon v-if="item.icon" class="mr-1">{{ item.icon }}</v-icon>
            {{ $t(item.label) }}
          </v-btn>
        </template>

        <v-menu offset-y>
          <template #activator="{ on }">
            <v-btn depressed btn v-on="on">
              <v-icon>mdi-translate</v-icon>
              <span v-if="$vuetify.breakpoint.name != 'xs'" class="ml-2">
                <v-icon class="ml-2">mdi-menu-down</v-icon>
              </span>
            </v-btn>
          </template>

          <v-list>
            <v-list-item :to="switchLocalePath('ja')">
              <v-list-item-title>日本語</v-list-item-title>
            </v-list-item>
            <v-list-item :to="switchLocalePath('en')">
              <v-list-item-title>English</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>

        
      </v-app-bar>
    </div>

    <v-main>
      <nuxt />
    </v-main>

    <v-footer :dark="true" class="mt-5">
      <v-container>
        <p class="text-center my-5">
          {{ $t(footer) }}
        </p>
      </v-container>
    </v-footer>

    <v-btn
      v-show="fab"
      v-scroll="onScroll"
      fab
      dark
      fixed
      bottom
      right
      large
      color="error"
      @click="toTop"
    >
      <v-icon>mdi-arrow-up</v-icon>
    </v-btn>
  </v-app>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import firebase from '../plugins/firebase'
import FullTextSearch from '~/components/search/FullTextSearch.vue'

@Component({
  components: {
    FullTextSearch,
  },
})
export default class search extends Vue {
  fab: boolean = false

  drawer: boolean = false
  baseUrl: string = process.env.BASE_URL || ''
  title: any = this.$t(process.env.siteName as any)

  footer: any = process.env.footer

  onScroll(e: any): void {
    if (typeof window === 'undefined') return
    const top = window.pageYOffset || e.target.scrollTop || 0
    this.fab = top > 20
  }

  toTop(): void {
    // @ts-ignore
    this.$vuetify.goTo(0)
  }

  get menu(): any[] {
    return [
      {
        label: "detail",
        to: this.localePath({ name: 'advanced' }),
      },
      
      {
        label: "category",
        to: this.localePath({ name: 'category' }),
      },
      {
        label: "about_",
        to: this.localePath({
          name: 'page-slug',
          params: { slug: 'about' },
        }),
      }
    ]
  }

  get isMobile() {
    if (['xs', 'sm'].includes((this as any).$vuetify.breakpoint.name)) {
      return true
    } else {
      return false
    }
  }
}
</script>

<style>
tbody tr:nth-of-type(odd) {
  background-color: rgba(0, 0, 0, 0.05);
}
* {
  text-transform: none !important;
}
a {
  text-decoration: none !important;
}
</style>
