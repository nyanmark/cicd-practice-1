const gulp = require('gulp');
const cleanCss = require('gulp-clean-css');
const minify = require("gulp-minify");

// minify CSS files
gulp.task('build-css', () => {
    return gulp.src('src/**/*.css')
    .pipe(cleanCss())
    .pipe(gulp.dest('build/'));
});

// minify JS files
gulp.task('build-js', () => {
    return gulp.src('src/**/*.js')
    .pipe(minify({
        ext: {
            min: '.js' // Set the file extension for minified files to just .js
        },
        noSource: true // Don’t output a copy of the source file
    }))
    .pipe(gulp.dest('build/'));
});

// copy all the other files to build
gulp.task('copy-remaining-files', () => {
    return gulp.src(['src/**/*.*', '!src/**/*.css', '!src/**/*.js'])
    .pipe(gulp.dest('build/'));
});

gulp.task("session-start", (cb) => {
    return gulp.series('build-css')(cb), gulp.series('build-js')(cb), gulp.series('copy-remaining-files')(cb);
});

gulp.task('default', gulp.series('session-start'));