'use strict';
angular.
    module('homepage').
        factory('PublicTask', function($resource){
            var url = '/api/tasks/public/'
            return $resource(url, {}, {
                query: {
                    method: "GET",
                    params: {},
                    isArray: true,
                    cache: false,
                    transformResponse: function(data, headersGetter, status){
                        console.log(data)
                        var finalData = angular.fromJson(data)
                        return finalData
                    }
                    // interceptor
                },
                get: {
                    method: "GET",
                    isArray: false,
                    cache: false,
                }
            })

        })
angular.
    module('homepage').
        factory('PrivateTask', function($resource){
            var url = '/api/tasks/:id/private/'
            return $resource(url, {}, {
                query: {
                    method: "GET",
                    params: {},
                    isArray: true,
                    cache: false,
                    transformResponse: function(data, headersGetter, status){
                        console.log(data)
                        var finalData = angular.fromJson(data)
                        return finalData
                    }
                    // interceptor
                },
                get: {
                    method: "GET",
                    params: {"user": "@id"},
                    isArray: false,
                    cache: false,
                }
            })

        })

angular.module('homepage').
    component('homepage', {
        templateUrl : "dashboard.html",
        controller: function(PrivateTask, PublicTask, $cookies, $http, $location, $routeParams, $rootScope, $scope){
            var tokenExists = $cookies.get("token")
            var usernameExists = $cookies.get("username")
            if (tokenExists) {

                $scope.loggedin = true
                $scope.order = '-created_at'
                $scope.username = $cookies.get("username")

                PublicTask.query( function(data){
                    $scope.publictaskList = data

                })
                
                var userid = $cookies.get("userid")
                console.log(userid)
                PrivateTask.query({"id": userid}, function(data){
                    $scope.privateTaskList = data

                })

                
                

            } else {
                $location.path("/login/")
            }
                
                
        } 
    })

angular
  .module('homepage')
  .filter('timeAgo', ['$interval', function ($interval){
    // trigger digest every 60 seconds
    $interval(function (){}, 60000);

    function fromNowFilter(time){
      return moment(time).fromNow();
    }

    fromNowFilter.$stateful = true;
    return fromNowFilter;
  }]);
    