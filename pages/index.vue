<template>
  <div>
    <section class="mb-5">
      <v-parallax :src="top" height="300">
        <v-layout column align-center justify-center class="white--text">
          <h1 class="white--text mb-2 display-1 text-center">
            <b>{{ siteName }}</b>
          </h1>
          <v-btn
            large
            class="mt-5"
            :to="localePath({ name: 'search' })"
            color="primary"
            >{{ $t('try_out') }}</v-btn
          >
        </v-layout>
      </v-parallax>
    </section>

    <v-container class="mt-10">
      <div class="mb-5 pb-5 text-center">
        <!-- <h1>{{ $t(siteName) }}</h1> -->
        <p class="py-5" v-html="siteDesc"></p>
      </div>

      <div v-if="items.length > 0">
        <h3 class="mt-5 mb-10 text-center">{{ $t('menu') }}</h3>

        <v-row class="mb-10">
          <v-col v-for="(obj, key) in items" :key="key" cols="12" :sm="6">
            <v-card flat outlined no-body class="mb-4 pa-4">
              <template v-if="obj.href">
                <a :href="obj.href" target="_blank">
                  <template v-if="obj.img">
                    <div
                      class="text-center grey lighten-2"
                      style="height: 150px"
                    >
                      <v-img contain style="height: 150px" :src="obj.img" />
                    </div>
                  </template>
                  <template v-else>
                    <div
                      class="text-center grey lighten-2 pa-10"
                      style="height: 150px"
                    >
                      <v-icon size="75">{{ obj.icon }}</v-icon>
                    </div>
                  </template>
                </a>
                <div class="pa-4">
                  <a :href="obj.href" target="_blank">
                    <h4>{{ obj.label }}</h4>
                  </a>

                  <p v-if="obj.description" class="mt-2 mb-0">
                    {{ obj.description }}
                  </p>
                </div>
              </template>
              <template v-else>
                <v-row>
                  <v-col md="4" cols="12">
                    <nuxt-link :to="localePath(obj.path)">
                      <!-- lighten-2 grey -->
                      <div class="text-center pa-10" style="height: 150px">
                        <v-icon size="75">{{ obj.icon }}</v-icon>
                      </div>
                    </nuxt-link>
                  </v-col>
                  <v-col>
                    <div class="px-4">
                      <nuxt-link :to="localePath(obj.path)">
                        <h4>{{ obj.label }}</h4>
                      </nuxt-link>

                      <p
                        v-if="obj.description"
                        class="mt-2 mb-0"
                        v-html="obj.description"
                      ></p>
                    </div>
                  </v-col>
                </v-row>
              </template>
            </v-card>
          </v-col>
          <v-col
            v-if="false"
            v-for="(obj, key) in items"
            :key="key"
            cols="12"
            :sm="3"
          >
            <v-card flat no-body class="mb-4">
              <template v-if="obj.href">
                <a :href="obj.href" target="_blank">
                  <template v-if="obj.img">
                    <div
                      class="text-center grey lighten-2"
                      style="height: 150px"
                    >
                      <v-img contain style="height: 150px" :src="obj.img" />
                    </div>
                  </template>
                  <template v-else>
                    <div
                      class="text-center grey lighten-2 pa-10"
                      style="height: 150px"
                    >
                      <v-icon size="75">{{ obj.icon }}</v-icon>
                    </div>
                  </template>
                </a>
                <div class="pa-4">
                  <a :href="obj.href" target="_blank">
                    <h4>{{ obj.label }}</h4>
                  </a>

                  <p v-if="obj.description" class="mt-2 mb-0">
                    {{ obj.description }}
                  </p>
                </div>
              </template>
              <template v-else>
                <nuxt-link :to="localePath(obj.path)">
                  <div
                    class="text-center grey lighten-2 pa-10"
                    style="height: 150px"
                  >
                    <v-icon size="75">{{ obj.icon }}</v-icon>
                  </div>
                </nuxt-link>
                <div class="pa-4">
                  <nuxt-link :to="localePath(obj.path)">
                    <h4>{{ obj.label }}</h4>
                  </nuxt-link>

                  <p
                    v-if="obj.description"
                    class="mt-2 mb-0"
                    v-html="obj.description"
                  ></p>
                </div>
              </template>
            </v-card>
          </v-col>
        </v-row>
      </div>

      <v-card flat class="my-5" v-if="false">
        <v-card-title>
          <h2>{{ $t('updates') }}</h2>
        </v-card-title>
        <v-card-text>
          <ul class="text--primary">
            <li>2021年XX月XX日: プロトタイプシステムを公開しました。</li>
          </ul>
        </v-card-text>
      </v-card>

      <br />
    </v-container>

    <v-sheet color="grey lighten-3" class="">
      <v-container class="mt-5 py-10">
        <v-card-title>
          <h2>{{ $t('updates') }}</h2>
        </v-card-title>
        <v-card-text>
          <ul class="text--primary">
            <li>2021年12月3日: システムを公開しました。</li>
          </ul>
        </v-card-text>
      </v-container>
    </v-sheet>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'

@Component({})
export default class about extends Vue {
  baseUrl: any = process.env.BASE_URL
  siteName: any = (this as any).$t(process.env.siteName)
  siteDesc: any = process.env.siteDesc
  top: any = process.env.top
  visualization: any = process.env.visualization

  items: any = []

  head() {
    const title = this.siteName
    return {
      titleTemplate: null,
      title,
    }
  }
}
</script>
