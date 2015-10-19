'use strict';

var pilightsApp = angular.module('pilightsApp', [
]);

pilightsApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      otherwise({
        redirectTo: '/'
      });
  }]);
