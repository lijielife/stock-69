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

.controller('IndustryDetailCtrl', function($scope, $rootScope, $stateParams, $http) {
	var sortField = $rootScope.sortField;
	if(!sortField){
		sortField = 'pe_lyr';
	}
	
	var sortDetail = '';
	if(sortField == 'pe_lyr'){
		sortDetail = '排序规则：[市盈率(PE)LYR]越低越靠前';
	} else if(sortField == 'pe_ttm'){
		sortDetail = '排序规则：[市盈率(PE)TTM]越低越靠前';
	} else if(sortField == 'pb'){
		sortDetail = '排序规则：[市净率(PB)TTM]越低越靠前';
	} else if(sortField == 'psr'){
		sortDetail = '排序规则：[市销率(PSR)TTM]越低越靠前';
	}
	
	$rootScope.sortDetail = sortDetail;
	
	var url = '/industry/' + $stateParams.icode + '/' + sortField;
    $http.get(url)
    .success(function(data) {
        if(data){
            $scope.industry = data;
            $scope.title = data.name;
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

.controller('BookmarksCtrl', function($scope, $rootScope, $http) {
	if($rootScope.stars){
		
	} else {
		$rootScope.stars = new Array()
	}
})

.controller('SettingsCtrl', function($scope, $http) {
	
})

.controller('SortFieldSelectCtrl', function($scope, $rootScope, $http) {
	$scope.click = function(event){
		$rootScope.sortField = event.target.value;
	}
});

