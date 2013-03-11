// declare a module
angular.module('tasklist', []).config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/', {
    templateUrl: 'partials/home.html',
  });
  $routeProvider.when('/add', {
    templateUrl: 'partials/add.html',
  });
  $routeProvider.when('/list', {
    templateUrl: 'partials/list.html',
    controller: TaskListCtrl
  });
  $routeProvider.when('/test', {
    templateUrl: 'partials/test.html',
  });
}]);


function TaskListCtrl($scope, $http) {
  $http.get('/tasks.json').success(function(response) {
    $scope.tasks = response;
  });
 
}
