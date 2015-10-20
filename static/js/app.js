'use strict';

var pilightsApp = angular.module('pilightsApp', [
  'ngRoute'
]);

pilightsApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      otherwise({
        redirectTo: '/'
      });
  }]);
