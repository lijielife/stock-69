angular.module('starter.controllers', [])

.controller('IndustryCtrl', function($scope, $http) {
	var url = '/industrys/0';
    $http.get(url)
    .success(function(data) {
        if(data){
            $scope.industrys = data;
        }
    })
})

.controller('IndustryDetailCtrl', function($scope, $stateParams, $http) {
	var url = '/industry/' + $stateParams.icode;
    $http.get(url)
    .success(function(data) {
        if(data){
            $scope.industry = data;
        }
    })
})

.controller('StockCtrl', function($scope, $stateParams, $http) {
	var url = '/stock/' + $stateParams.code;
    $http.get(url)
    .success(function(data) {
        if(data){
            $scope.stock = data;
        }
    })
})

.controller('BookmarksCtrl', function($scope, $http) {
  
})

.controller('SettingsCtrl', function($scope, $http) {

});
