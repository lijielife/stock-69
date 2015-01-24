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
	
	var sfn = '';
	if(sortField == 'pe_lyr'){
		sfn = '市盈率(PE)LYR';
	} else if(sortField == 'pe_ttm'){
		sfn = '市盈率(PE)TTM';
	} else if(sortField == 'pb'){
		sfn = '市净率(PB)TTM';
	} else if(sortField == 'psr'){
		sfn = '市销率(PSR)TTM';
	}
	$scope.sfn = sfn;
	
	var url = '/industry/' + $stateParams.icode + '/' + sortField;
    $http.get(url)
    .success(function(data) {
        if(data){
            $scope.industry = data;
            $scope.title = data.name;
        }
    })
})

.controller('StockCtrl', function($scope, $rootScope, $stateParams, $http) {
	var url = '/stock/' + $stateParams.code;
    $http.get(url)
    .success(function(data) {
        if(data){
            $scope.stock = data;
            $scope.starIcon = 'ion-ios7-star-outline';
            $scope.starTxt = '收藏';
            
            if(!$rootScope.stars){
    			$rootScope.stars = new Array()
    		}
            
            var stars = $rootScope.stars;
    		for(i = 0; i < stars.length; i++){
    			var stock = stars[i];
    			
    			if(data.code == stock.code){
    				$scope.starIcon = 'ion-ios7-star';
    				$scope.starTxt = '已收藏';
    				return;
    			}
    		}
        }
    })
})

.controller('BookmarksCtrl', function($scope, $rootScope, $http) {
	if(!$rootScope.stars){
		$rootScope.stars = new Array()
	}
})

.controller('SettingsCtrl', function($scope, $http) {
	
})

.controller('StarSelectCtrl', function($scope, $rootScope, $http) {
	$scope.click = function(event){
		if(!$rootScope.stars){
			$rootScope.stars = new Array()
		}
		
		var ids = event.target.id;
		var idName = ids.split(',');
		var star = {code:idName[0], name:idName[1]};
		
		// 改图标，改已收藏

		var stars = $rootScope.stars;
		for(i = 0; i < stars.length; i++){
			var stock = stars[i];
			
			if(stock.code == star.code){
				return;
			}
		}
		
		stars[stars.length] = star;
		$scope.starIcon = 'ion-ios7-star';
		$scope.starTxt = '已收藏';
	}
})

.controller('SortFieldSelectCtrl', function($scope, $rootScope, $http) {
	$scope.click = function(event){
		$rootScope.sortField = event.target.value;
	}
});

