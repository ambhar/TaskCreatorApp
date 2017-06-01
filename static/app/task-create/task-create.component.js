'use strict';

angular.module('taskCreate').
    component('taskCreate', {
        templateUrl : "task-create.html",
        controller: function($cookies, $http, $location, $routeParams, $scope, $filter){

           var taskCreateUrl = 'api/tasks/create/'
            
            
            $scope.taskCreateMessage = "";
            var tokenExists = $cookies.get("token")
            if (tokenExists) {
                
                $scope.doCreateTask = function(task){
                    console.log(task);
                    if(task.title && task.description && task.deadline && task.tasktype){
                        task.deadline = $filter('date')(new Date($scope.task.deadline),'yyyy-MM-dd');
                        var reqConfig = {
                            method: "POST",
                            url: taskCreateUrl,
                            data: {
                                user :  $cookies.get("userid"), //$cookies.get("merchant_id")
                                title : task.title,
                                description : task.description,
                                deadline : task.deadline,
                                is_private : task.tasktype
                            },
                            headers: {}
                        }

                        var taskCreateRequestAction = $http(reqConfig)

                        taskCreateRequestAction.success(function(r_data, r_status, r_headers, r_config) {
                            $location.path("/homepage/") //+ $cookies.get("merchant_id") +"/customers"

                        })
                        taskCreateRequestAction.error(function(e_data, e_status, e_headers, e_config) {
                            console.log(e_data)
                            $scope.taskCreateMessage = "Error in creating task."
                        })

                    }
                }
            
           } else {
                $location.path("/login/")
           }
        }
    })
    