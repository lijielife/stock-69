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
	var sfn = '';
	if(sortField == 'pe_lyr'){
		sfn = '市盈率(PE)LYR';
		sortDetail = '当前排序规则：【市盈率(PE)LYR】'; 
	} else if(sortField == 'pe_ttm'){
		sfn = '市盈率(PE)TTM';
		sortDetail = '当前排序规则：【市盈率(PE)TTM】';
	} else if(sortField == 'pb'){
		sfn = '市净率(PB)TTM';
		sortDetail = '当前排序规则：【市净率(PB)TTM】';
	} else if(sortField == 'psr'){
		sfn = '市销率(PSR)TTM';
		sortDetail = '当前排序规则：【市销率(PSR)TTM】';
	}
	$scope.sfn = sfn;
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

