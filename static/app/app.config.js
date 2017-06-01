'use strict';

angular.module("taskapp").
    config(function($routeProvider, $resourceProvider, $locationProvider,$httpProvider, $interpolateProvider) {
            $interpolateProvider.startSymbol('{$');
            $interpolateProvider.endSymbol('$}');
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $resourceProvider.defaults.stripTrailingSlashes =  false ;
            $routeProvider
                .when("/homepage/", {
                    template: "<homepage></homepage"
                }).
                when("/", {
                    template: "<user-login></user-login>"
                }).
                when("/login/", {
                    template: "<user-login></user-login>"
                }).
                when("/signup/", {
                    templateUrl: "signup.html"
                }).
                when("/create", {
                    template: "<task-create></task-create>"
                }).
                when("/accounts/signup/", {
                    template: "signup.html"
                }).
                otherwise({
                  template: ""
                })
                $locationProvider.html5Mode(true) ;
        

    }).controller('appController', function ($scope) {
        $scope.name = "dsad";
        console.log("Hello world");

    });
