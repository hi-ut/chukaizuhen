<template>
  <div>
    <v-footer :dark="true" class="py-5">
      <v-container>
        <v-row>
          <v-col cols="12" :md="3" v-for="(item, key) in menu" :key="key">
            <template v-if="item.to">
              <nuxt-link
                style="color: white; font-size: smaller"
                depressed
                :to="localePath(item.to)"
                exact
                >{{ $t(item.label) }}
              </nuxt-link>
            </template>
            <template v-else>
              <a
                style="color: white; font-size: smaller"
                depressed
                :href="item.href"
                :target="item.target || ''"
                exact
                >{{ $t(item.label) }}
                <template v-if="item.target">
                  <v-icon class="ml-1">mdi-exit-to-app</v-icon>
                </template></a
              >
            </template>
          </v-col>
          <v-col cols="12" :md="3">
            <template v-if="$i18n.locale !== 'en'">
              <nuxt-link
                style="color: white; font-size: smaller"
                :to="switchLocalePath('en')"
              >
                English
              </nuxt-link>
            </template>
            <template v-else>
              <nuxt-link
                style="color: white; font-size: smaller"
                :to="switchLocalePath('ja')"
              >
                日本語
              </nuxt-link>
            </template>
          </v-col>
        </v-row>
      </v-container>
    </v-footer>

    <v-footer :dark="true" style="background-color: black">
      <v-container>
        <p class="text-center my-5">
          {{ $t(footer) }}
        </p>
      </v-container>
    </v-footer>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'nuxt-property-decorator'

@Component({
  components: {},
})
export default class License extends Vue {
  footer: any = process.env.footer

  menu: any = process.env.menu
}
</script>
