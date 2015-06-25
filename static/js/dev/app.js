'use strict';

/**
 * @ngdoc object
 * @name conferenceApp
 * @requires $routeProvider
 * @requires conferenceControllers
 * @requires ui.bootstrap
 *
 * @description
 * Root app, which routes and specifies the partial html and controller depending on the url requested.
 *
 */
var app = angular.module('notebookApp',
    ['noteControllers', 'ngRoute', 'ui.bootstrap']).
    config(['$routeProvider',
        function ($routeProvider) {
            $routeProvider.
                when('/conference', {
                    templateUrl: '/partials/show_conferences.html'//,controller: 'ShowConferenceCtrl'
                }).
                when('/conference/create', {
                    templateUrl: '/partials/create_conferences.html'//,controller: 'CreateConferenceCtrl'
                }).
                when('/conference/detail/:websafeConferenceKey', {
                    templateUrl: '/partials/conference_detail.html'//,controller: 'ConferenceDetailCtrl'
                }).
                when('/profile', {
                    templateUrl: '/partials/profile.html'//,controller: 'MyProfileCtrl'
                }).
                when('/search', {
                    templateUrl: '/partials/search.html'                    
                }).
                when('/category/:subcategory', {
                    templateUrl: '/partials/category.html',
                    controller: 'NoteCategoryCtrl'
                }).
                when('/viewnote/:notekey', {
                    templateUrl: '/partials/viewnote.html'                    
                }).
                when('/', {
                    templateUrl: '/partials/home.html',
                    controller: 'HomeSliderCtrl'
                }).
                otherwise({
                    redirectTo: '/'
                });
        }]);

/**
 * @ngdoc filter
 * @name startFrom
 *
 * @description
 * A filter that extracts an array from the specific index.
 *
 */
app.filter('startFrom', function () {
    /**
     * Extracts an array from the specific index.
     *
     * @param {Array} data
     * @param {Integer} start
     * @returns {Array|*}
     */
    var filter = function (data, start) {
        return data.slice(start);
    }
    return filter;
});


/**
 * @ngdoc constant
 * @name HTTP_ERRORS
 *
 * @description
 * Holds the constants that represent HTTP error codes.
 *
 */
app.constant('HTTP_ERRORS', {
    'UNAUTHORIZED': 401
});