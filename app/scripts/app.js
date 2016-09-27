'use strict';

/**
 * @ngdoc overview
 * @name pi1App
 * @description
 * # pi1App
 *
 * Main module of the application.
 */
angular
  .module('pi1App', [
    'ngAnimate',
    'ngAria',
    'ngCookies',
    'ngMessages',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/sobreNosotros', {
        templateUrl: 'views/sobreNosotros.html',
        controller: 'SobreNosotrosCtrl',
        controllerAs: 'sobreNosotros'
      })
      .when('/contact', {
        templateUrl: 'views/contact.html',
        controller: 'ContactCtrl',
        controllerAs: 'contact'
      })
      .when('/login', {
        templateUrl: 'views/login.html',
        controller: 'LoginCtrl',
        controllerAs: 'login'
      })
      .when('/testimonios', {
        templateUrl: 'views/testimonios.html',
        controller: 'TestimoniosCtrl',
        controllerAs: 'testimonios'
      })
       .when('/noticias', {
        templateUrl: 'views/noticias.html',
        controller: 'NoticiasCtrl',
        controllerAs: 'noticias'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
